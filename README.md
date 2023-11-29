# actiontry
**Understanding Github Actions And Using Beeware Briefcase In A Github Workflow**

## Intro 
This project is for my own understanding and memory, and does the following : 

1. Uses [beeware briefcase](https://beeware.org/project/projects/tools/briefcase/) to generate appimage file in a github workflow
2. shows probably the simplest way to use a github action to create release with a binary installation file

## How to use

Check the two workflows in the [.github/workflows](https://github.com/rahlumin/actiontry/tree/maser/.github/workflows) directory of this repo. Both these workflows are set to be run manually. 

1. **appimage.yml:** shows a very simple github workflow for creating the appimage  from the code in the repository, and releases it as a draft.
                 This particular project uses beeware briefcase for build , and generates an `Appimage` for linux systems, you can use any build options of choice. 
                 From `briefcase` perspective, The important thing to note here is that briefcase config file `pyproject.toml` 
                  should be present at the root of the project and the source should be in `src` directory

 2. **workflow2.yml** includes all the code in appimage.yml , but goes one step further and takes user input for a tag. 
                      Then it uses this info to create a public release with all the   files. 
                      This is  the more useful, but slightly more complex than appimage.yml
 3. **workflowmulti.yml** Includes all the code in above two workflows, but also creates a  `.deb` file along with the usual `.Appimage` file. 
                          Both are created in a single job which is run on a Ubuntu runner as before. This makes it a simple extension of above workflows. Had we needed to create an i                                installer for Windows, we would have needed a windows runner as well. 
       

## Outro 
&copy; Rahul Singh

