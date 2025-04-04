from pr_agent import cli
from pr_agent.config_loader import get_settings
import os

def main():

    # Setting the configurations
    provider = "github" # github/gitlab/bitbucket/azure_devops
    user_token = os.getenv("GITHUB_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")
    pr_url = os.getenv("PR_URL")
    command = os.getenv("COMMAND")
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    print(f"Using {provider} as the provider")
    print(f"Using {pr_url} as the PR URL")
    print(f"Using {command} as the command")

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)


if __name__ == '__main__':
    print("Running the PR agent...")
    main()
