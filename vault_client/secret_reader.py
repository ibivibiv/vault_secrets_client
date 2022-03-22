import hvac



class Secrets():

    def __init__(self, url, token):
        self.client = hvac.Client(url=url, token=token)


    def read(self, mount, path):
        read_secret_result = self.client.secrets.kv.v2.read_secret(
            mount_point=mount,
            path=path
        )

        data = read_secret_result['data']

        return data
