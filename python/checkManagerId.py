import appconstants
import requests
if __name__ == "__main__":
    if requests.get(appconstants.managerBasicInfoUrl.replace("{manager_id}", open(appconstants.managerIdDir, "r").read())).status_code == 404:
        print()