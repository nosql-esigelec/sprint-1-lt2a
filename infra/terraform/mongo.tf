
resource "google_compute_firewall" "mongo_firewall_rule" {
  name    = "mongo-allow-specific-ips-on-ports"
  network = "default"

  allow {
    protocol = "tcp"
    ports = ["27017"] # Port Management
  }

  source_ranges = var.whitelisted_ips # IP Whitelisting
  target_tags   = ["http-server","https-server"] # Firewall rule applies only to instances with this tag
}


resource "google_compute_instance" "mongo_node" {
  count        = var.num_nodes # the number of instances to provision
  name         = "mongo-node-${count.index}"
  machine_type = "e2-medium" # machine type of each node
  zone = "europe-west1-b" # The instance zone(not the region)
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

                              sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/disk/by-id/google-test-disk
                              sudo mkdir -p /mongo/data
                              sudo mount -o discard,defaults /dev/disk/by-id/google-test-disk /mongo/data
                              sudo chown -R ${var.username}:${var.username} /mongo/data
                              echo UUID=$(sudo blkid -s UUID -o value /dev/disk/by-id/google-test-disk) /mongo/data ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab

                              EOF
    metadata = {
    ssh-keys = "${var.username}:${file(var.public_key_path)}"
  }
}

resource "google_compute_disk" "mongo_disk" {
  count = var.num_nodes
  name = "mongo-disk-${count.index}"
  type = "pd-standard"
  zone = "europe-west1-b"
  size = 5 # specify the size of the disk in GB
  labels = {
    environment = "dev"
  }
  physical_block_size_bytes = 4096
}

resource "google_compute_attached_disk" "mongo_attached_disk" {
  count = var.num_nodes
  disk     = google_compute_disk.mongo_disk[count.index].id
  instance = google_compute_instance.mongo_node[count.index].id
  zone     = google_compute_instance.mongo_node[count.index].zone
}

