# TODO: Complete this terraform file to setup the right configurations

resource "google_compute_firewall" "mongo_firewall_rule" {
  name    = "mongo-allow-specific-ips-on-ports"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = "TO COMPLETE" # Port Management
  }

  source_ranges = "TO COMPLETE" # IP Whitelisting
  target_tags   = ["http-server","https-server"] # Firewall rule applies only to instances with this tag
}


resource "google_compute_instance" "mongo_node" {
  count        = var.num_nodes # the number of instances to provision
  name         = "mongo-node-${count.index}"
  machine_type = "e2-medium" # machine type of each node
  zone         = "TO COMPLETE" # The instance zone(not the region)
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
    ssh-keys = "TO COMPLETE:${file(var.public_key_path) }"
  }
}
