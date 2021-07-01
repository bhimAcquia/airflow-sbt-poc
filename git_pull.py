import git
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
print("hello python")

def git_call() :
    print("git_call")
    #git_dir = "https://github.com/bhimAcquia/airflow-sbt-poc.git"
    #repo = Repo(git_dir)
    #repo.config_reader()             # get a config reader for read-only access
    #repo.remotes.pull()
    git_dir = ""
    g = git.Git( git_dir )
    #reset to overwrite the files
    print("git reset --hard")
    g.reset('--hard')
    print("git pull")
    g.pull()
    #git.cmd.Git().pull(git_dir,'master')
    print("git pull done")

git_call()
