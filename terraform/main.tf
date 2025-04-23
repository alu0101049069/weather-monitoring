provider "aws" {
  region = "eu-north-1"  # Cambia según tu región
}

resource "aws_instance" "linux_server" {
  ami           = "ami-0d4f84b7313c8b114"  # Ubuntu 22.04 en eu-north-1
  instance_type = "t3.micro"
  key_name      = var.key_name
  tags = {
    Name = "MiServidorLinux"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y nginx"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file(var.private_key_path)
      host        = self.public_ip
    }
  }
}
