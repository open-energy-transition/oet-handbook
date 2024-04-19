import os

def delete_folders(base_directory, max_deletions):
    folders_deleted = 0

    # Iterate over the items in the base directory
    for item in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, item)

        # Check if it is a folder and not named 'template'
        if os.path.isdir(folder_path) and item != "template":
            files = os.listdir(folder_path)

            # Check if the folder has exactly 3 files and contains 'company.jpg'
            if len(files) == 2 :
                # Delete the folder
                for file in files:
                    os.remove(os.path.join(folder_path, file))
                os.rmdir(folder_path)
                print(f"Deleted folder: {folder_path}")
                folders_deleted += 1

                # Stop if we have deleted the maximum number of folders requested
                if folders_deleted >= max_deletions:
                    break

    print(f"Total folders deleted: {folders_deleted}")

# Settings



def main():
    base_directory = "/home/akshat/oet-handbook/docs"  # Update this path to your directory
    max_deletions = 2000  # Update this number to how many folders you want to delete

    # Run the function
    delete_folders(base_directory, max_deletions)


if __name__ == "__main__":
    main()