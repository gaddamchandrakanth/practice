terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}
provider "aws" {
    region = "us-east-1"
}
resource "aws_s3_bucket" "testing" {
    bucket = "chandu9963291-123"
    tags={
        Name="testing"
        Environment= "testing"
    }
