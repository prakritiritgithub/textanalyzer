provider "aws" {
  region="us-east-1"
  access_key="AKIAYD6BO3N5AABL6KDM"
  secret_key="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"
}

resource "aws_instance" "web" {
  ami           = "ami-041feb57c611358bd"
  instance_type = "t3.micro"

  tags = {
    Name = "TRIDIPAVM"
  }
}



