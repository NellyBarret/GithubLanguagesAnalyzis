import urllib.request
import json
import requests
base_url = "https://api.github.com/"

def login():
  login = requests.get('https://api.github.com/', auth=('NellyBARRET', '27juillet2018'))

def get_languages(owner, project_name):
  complete_url = base_url+"repos/"+owner+"/"+project_name+"/languages"
  contents = urllib.request.urlopen(complete_url).read()
  # print(contents)
  return json.loads(contents)

def getRepositoriesSince(since):
  print("getting repo since " + str(since))
  data = []
  complete_url = base_url + "repositories?since="+str(since)

  contents = requests.get(complete_url, auth=('NellyBARRET', 'XXX'))

  # contents = requests.get(complete_url)
  return contents.json()


def getAllRepositories():
  local_repo = getRepositoriesSince(1)
  all_repositories = []
  all_repositories.append(local_repo[0])
  if type(local_repo) is list:
    repo_id = local_repo[len(local_repo)-1]["id"]
  else:
    repo_id = local_repo["id"]
  while(local_repo and repo_id < 1000):
    local_repo = getRepositoriesSince(repo_id)
    repo_id = local_repo[len(local_repo)-1]["id"]
    all_repositories.append(local_repo[0])
  return all_repositories

def write_in_file(data):
  print("begin")
  #f=open("data.json","w+")
  formated_data = json.dumps(data)
  f = open("data.json","w")
  f.write(formated_data)
  f.close()
  print("finished")

if __name__ == "__main__":
  owner = "NellyBARRET"
  project_name = "bejeweled"
  #login()
  # languages = get_languages(owner, project_name)
  # write_in_file(languages)
  all_r = getAllRepositories()
  write_in_file(all_r)