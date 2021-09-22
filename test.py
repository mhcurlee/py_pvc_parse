from jinja2 import Template
from yaml import safe_load

# base vars
namespace_name = "myproject"
server = "nfs01.curlee.local"
basepath = "/pub/base/"


# init data list
data = []


# render template
def gen_yaml(name,size,mode,server,path): 
  ''' Function to render yaml from template'''
  print(template.render(name=name,size=size, mode=mode, server=server, path=path))


# Start
if __name__ == "__main__":

  # Read template file
  with open('pv.yaml') as file_:
      template = Template(file_.read())


  # Read pvc file
  with open('pvc.yaml') as file_:
      pvc_filedata = file_.read()
      pvc_data = safe_load(pvc_filedata)
      

  # loop through list of dicts
  for item in pvc_data['items']:
    item_dict = {
      "name": namespace_name + "-" + item['metadata']['name'] + "-pv", 
      "size": item['spec']['resources']['requests']['storage'],
      "mode": item['spec']['accessModes'][0],
      "server": server,
      "path": basepath + namespace_name + "/" + item['metadata']['name']
      }
    data.append(item_dict)


  # loop through array and render template
  for item in data:
    gen_yaml(item["name"], item["size"], item["mode"], item["server"], item["path"])


