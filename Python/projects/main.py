from jira import JIRA
import requests

class AlmJiraIntegration:
    def __init__(self, jira_server, alm_username, alm_password, alm_base_url):
        self.jira = JIRA(server=jira_server, options={"verify": False})
        self.alm_username = alm_username
        self.alm_password = alm_password
        self.alm_base_url = alm_base_url

    def get_alm_project_data(self, project_id):
        url = f"{self.alm_base_url}/api/projects/{project_id}"
        response = requests.get(url, auth=(self.alm_username, self.alm_password))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def display_alm_data_in_jira_issue(self, issue_key, alm_data):
        # Implement logic to display ALM data within a JIRA issue
        # For example, you can use JIRA's custom fields or comments
        self.jira.add_comment(issue_key, f"ALM Data: {alm_data}")

# Example usage
if __name__ == "__main__":
    alm_jira_integration = AlmJiraIntegration(
        jira_server="https://your-jira-instance.com",
        alm_username="your-alm-username",
        alm_password="your-alm-password",
        alm_base_url="https://your-alm-instance.com"
    )

    project_id = "your-alm-project-id"
    alm_data = alm_jira_integration.get_alm_project_data(project_id)

    issue_key = "your-jira-issue-key"
    alm_jira_integration.display_alm_data_in_jira_issue(issue_key, alm_data)