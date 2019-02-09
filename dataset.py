import torch
import torchvision
import torchvision.transforms as transforms


def get_cifar10(batch_size, dataset_directory, dataloader_workers):
    # Prepare dataset for training
    train_transformation = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ])
    train_dataset = torchvision.datasets.CIFAR10(root=dataset_directory, train=True,
                                                 download=True, transform=train_transformation)

    # Use sampler for randomization
    training_sampler = torch.utils.data.SubsetRandomSampler(range(len(train_dataset)))

    # Prepare Data Loaders for training and validation
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, sampler=training_sampler,
                                               pin_memory=True, num_workers=dataloader_workers)

    return train_dataset, train_loader


def get_celeba(batch_size, dataset_directory, dataloader_workers):
    # At first, download this file into dataset_directory and unzip it:
    # https://drive.google.com/open?id=0B7EVK8r0v71pZjFTYXZWM3FlRnM
    train_transformation = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ])
    train_dataset = datasets.ImageFolder(dataset_directory + 'img_align_celeba', transform)

    # Use sampler for randomization
    training_sampler = torch.utils.data.SubsetRandomSampler(range(len(train_dataset)))

    # Prepare Data Loaders for training and validation
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, sampler=training_sampler,
                                               pin_memory=True, num_workers=dataloader_workers)

    return train_dataset, train_loader

