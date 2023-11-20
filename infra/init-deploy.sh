# TODO: Remove comments for neo4j on this file when you'll finish the configurations to apply in terraform and ansible
#!/bin/bash
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <environment> <username> <local_private_key_path>"
    exit 1
fi

ENVIRONMENT=$1
USERNAME=$2
PRIVATE_KEY_PATH=$3


# Function to update Ansible inventory with dynamic IPs
update_ansible_inventory() {
  local db="$1"
  shift
  local ips=("$@")
  echo "[${db}_cluster]" > $db.ini
  for i in "${!ips[@]}"; do
    ssh-keygen -f "$HOME/.ssh/known_hosts" -R "${ips[i]}"
    echo "${db}-node-$i ansible_host=${ips[i]}" >> $db.ini
  done

  # Add other groups and vars as needed
  echo "[${db}_cluster:vars]" >> $db.ini
  echo "ansible_user=$USERNAME" >> $db.ini
  echo "ansible_ssh_private_key_file=$PRIVATE_KEY_PATH" >> $db.ini
}


cd terraform
sed -i "s/username = \"username_to_replace\"/username = \"${USERNAME}\"/" environments/$ENVIRONMENT.tfvars
terraform init
terraform apply -auto-approve -var-file="environments/$ENVIRONMENT.tfvars"

mongo_ips=$(terraform output -json mongo_instance_ips | jq -r '.[]')
# neo4_ips=$(terraform output -json neo4j_instance_ips | jq -r '.[]')
sed -i "s/username = \"${USERNAME}\"/username = \"username_to_replace\"/" environments/$ENVIRONMENT.tfvars
cd ..



# Run Ansible playbooks
cd ansible

###############################
#            MONGO            # 
###############################
# Update Ansible inventory with Mongo IP addresses
update_ansible_inventory "mongo" $mongo_ips
# Install docker 
ansible-playbook -i mongo.ini tasks/docker.yml
# Install mongo 
ansible-playbook -i mongo.ini tasks/mongo.yml

###############################
#            NEO4J            # 
###############################
# # Update Ansible inventory with Neo4j IP addresses
# update_ansible_inventory "neo4j" $neo4j_ips
# # Install docker 
# ansible-playbook -i neo4j.ini tasks/docker.yml
# # Install neo4j 
# ansible-playbook -i neo4j.ini tasks/neo4j.yml

