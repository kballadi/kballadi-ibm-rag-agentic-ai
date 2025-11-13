# Configurable variables (change these instead of editing commands below)
$ResourceGroupName = 'MyResourceGroup'
$Location = 'eastus'
$VmName = 'MyVM'
$VmImage = 'UbuntuLTS'

# Configure default resource group and location for subsequent Azure CLI commands
az configure --defaults `
	group=$ResourceGroupName `
	location=$Location

# Create the resource group (idempotent)
az group create `
	--name $ResourceGroupName `
	--location $Location

# Option: let Azure CLI generate SSH keys (~/.ssh/id_rsa.pub) if not present
az vm create `
	--resource-group $ResourceGroupName `
	--name $VmName `
	--image $VmImage `
	--generate-ssh-keys
