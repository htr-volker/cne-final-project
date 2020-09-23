resource "aws_instance" "default" {
  # ubuntu 18.04
  ami = "ami-089cc16f7f08c4457"
  instance_type = "t2.medium"
  subnet_id = "${aws_subnet.default.id}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  associate_public_ip_address = true
  key_name = "Jenkins"
  tags = {
    Name = "Jenkins"  
  }

  root_block_device {
    volume_type = "gp2"
    volume_size = 20
  }
}