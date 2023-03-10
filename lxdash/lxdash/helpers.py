import pylxd

class LXDash():

    def __init__(self):
        self.client = pylxd.Client()

    def get_all_instances(self):
        instances = self.client.instances.all()
        return instances

    def get_client_resources(self):
        resources = self.client.resources
        return resources

    def get_instance_by_name(self, name: str):
        instance = self.client.instances.get(name)
        return instance
