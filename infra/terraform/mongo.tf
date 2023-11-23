# TODO: Complete this terraform file to setup the right configurations

resource "google_compute_firewall" "mongo_firewall_rule" {
  name    = "mongo-allow-specific-ips-on-ports"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["27017"] # Port Management
  }

  source_ranges = ["0.0.0.0/0"] # IP Whitelisting
  target_tags   = ["http-server","https-server"] # Firewall rule applies only to instances with this tag
}

#DNS name configuration
resource "google_dns_managed_zone" "mongodb_zone" {
  name     = "mongodb-zone"
  dns_name = "mongodb.gocod-esig-lt2a.com."  # Assurez-vous que ceci correspond à votre domaine DNS

}

resource "google_dns_record_set" "mongodb_node_0" {
  name         = "mongo-node-0.mongodb.gocod-esig-lt2a.com"
  type         = "A"
  ttl          = 300
  managed_zone = google_dns_managed_zone.mongodb_zone.name
  rrdatas      = ["34.163.154.242"]  # Remplacer par l'adresse IP du premier nœud
}

resource "google_dns_record_set" "mongodb_node_1" {
  name         = "mongo-node-1.mongodb.gocod-esig-lt2a.com"
  type         = "A"
  ttl          = 300
  managed_zone = google_dns_managed_zone.mongodb_zone.name
  rrdatas      = ["34.163.241.16"]  # Remplacer par l'adresse IP du deuxième nœud
}

# Hard disk creation for backup
resource "google_compute_disk" "mongodb_disk" {
  name  = "mongodb-disk"
  type  = "pd-ssd"
  zone  = "europe-west9-c"
  size  = 10
}

resource "google_compute_instance" "mongo_node" {
  count        = var.num_nodes # the number of instances to provision
  name         = "mongo-node-${count.index}"
  machine_type = "e2-medium" # machine type of each node
  zone         = "europe-west9-b" # The instance zone(not the region)
  tags         = ["http-server","https-server"] # Tags to connect instances to internet
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11" #OS for each VM
      labels = var.common_labels # Some labels to identify the resources
    }
  }

  network_interface {
    network = "default"
    access_config {
      
    }
  }
  metadata_startup_script = <<-EOF
                              echo "Creating user ${var.username}"
                              sudo useradd -m -s /bin/bash -G sudo ${var.username}
                              echo "Deactivating password for user ${var.username}"
                              sudo passwd -d ${var.username}
                              EOF
    metadata = {
    ssh-keys = "${var.username}:${file(var.public_key_path) }"
  }
}
