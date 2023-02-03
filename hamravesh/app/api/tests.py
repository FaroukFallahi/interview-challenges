from contextlib import suppress

from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
import docker

class RestDockerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.d = docker.from_env()
        self.request_data = {
                            "name":"unit-test-docker-rest-api",
                            "image":"alpine"  ,
                            "env": { "env1" : "val1", "env2" : "val2" },
                            "command": "sleep 1000"}


    def tearDown(self) :
        with suppress(Exception):
            container = self.d.containers.get(self.request_data['name'])
            container.stop()
            container.remove()


    def test_create_container(self):
        response = self.client.post(
            reverse('api:endpoint'),
            self.request_data,
            'json'
        )
        container = self.d.containers.get(self.request_data['name'])
        self.assertIsNotNone(container)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_container(self):
        container = self.d.containers.run(name=self.request_data['name'],image="alpine",detach=True)
        response = self.client.delete(
            reverse('api:endpoint_id', args = (self.request_data['name'],)),
        )
        containers = self.d.containers.list(all=True)
        self.assertTrue(container not in containers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
