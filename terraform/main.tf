terraform {
  required_version = ">= 1.0"
}

resource "local_file" "devops_info" {
  filename = "${path.module}/devops-info.txt"
  content  = "DevOps Mastery Challenge - Terraform"
}
