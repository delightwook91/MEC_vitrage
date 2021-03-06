# Copyright 2017 - Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class Connection(object):
    """Base class for storage system connections."""

    def __init__(self, conf, url):
        pass

    @property
    def active_actions(self):
        return None

    @property
    def events(self):
        return None

    @property
    def templates(self):
        return None

    @property
    def graph_snapshots(self):
        return None

    @property
    def webhooks(self):
        return None

    @abc.abstractmethod
    def upgrade(self, nocreate=False):
        raise NotImplementedError('upgrade is not implemented')

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError('disconnect is not implemented')

    @abc.abstractmethod
    def clear(self):
        raise NotImplementedError('clear is not implemented')


@six.add_metaclass(abc.ABCMeta)
class ActiveActionsConnection(object):
    @abc.abstractmethod
    def create(self, active_action):
        """Create a new action.

        :type active_action: vitrage.storage.sqlalchemy.models.ActiveAction
        """
        raise NotImplementedError('create active action is not implemented')

    @abc.abstractmethod
    def update(self, active_action):
        """Update an existing action.

        :type active_action: vitrage.storage.sqlalchemy.models.ActiveAction
        """
        raise NotImplementedError('update active action is not implemented')

    @abc.abstractmethod
    def query(self,
              action_type=None,
              extra_info=None,
              source_vertex_id=None,
              target_vertex_id=None,
              action_id=None,
              score=None,
              trigger=None,
              ):
        """Yields a lists of active actions that match filters.

        :rtype: list of vitrage.storage.sqlalchemy.models.ActiveAction
        """
        raise NotImplementedError('query active actions is not implemented')

    @abc.abstractmethod
    def delete(self,
               action_type=None,
               extra_info=None,
               source_vertex_id=None,
               target_vertex_id=None,
               action_id=None,
               score=None,
               trigger=None,
               ):
        """Delete all active actions that match the filters."""
        raise NotImplementedError('delete active actions is not implemented')


@six.add_metaclass(abc.ABCMeta)
class WebhooksConnection(object):

    @abc.abstractmethod
    def create(self, webhook):
        """Create a new webhook.

        :type webhook:
        vitrage.storage.sqlalchemy.models.Webhook
        """
        raise NotImplementedError('create webhook is not implemented')

    @abc.abstractmethod
    def query(self,
              id=None,
              project_id=None,
              is_admin_webhook=None,
              url=None,
              headers=None,
              regex_filter=None,
              ):
        """Yields a lists of webhooks that match filters.

        :rtype: list of vitrage.storage.sqlalchemy.models.Webhook
        """
        raise NotImplementedError('query webhook is not implemented')

    @abc.abstractmethod
    def delete(self, id=None):
        """Delete all webhooks that match the filters."""
        raise NotImplementedError('delete webhook is not implemented')


@six.add_metaclass(abc.ABCMeta)
class TemplatesConnection(object):

    @abc.abstractmethod
    def create(self, template):
        """Add a new template.

        :type template: vitrage.storage.sqlalchemy.models.Template
        """
        raise NotImplementedError('Create Template not implemented')

    @abc.abstractmethod
    def update(self, uuid, var, value):
        """update existing template.

        :type template: vitrage.storage.sqlalchemy.models.Template
        """
        raise NotImplementedError('Update Template not implemented')

    @abc.abstractmethod
    def query(self, name=None, file_content=None,
              uuid=None, status=None, status_details=None,
              template_type=None):
        """Yields a lists of templates that match filters.

        :type: list of vitrage.storage.sqlalchemy.models.Template
        """
        raise NotImplementedError('Query Templates not implemented')

    @abc.abstractmethod
    def delete(self, name=None, uuid=None):
        """Delete existing template

        :type: list of vitrage.storage.sqlalchemy.models.Template
        """
        raise NotImplementedError('Delete Templates not implemented')


@six.add_metaclass(abc.ABCMeta)
class EventsConnection(object):
    def create(self, event):
        """Create a new event.

        :type event: vitrage.storage.sqlalchemy.models.Event
        """
        raise NotImplementedError('create event is not implemented')

    def update(self, event):
        """Update an existing event.

        :type event: vitrage.storage.sqlalchemy.models.Event
        """
        raise NotImplementedError('update event is not implemented')

    def query(self,
              event_id=None,
              collector_timestamp=None,
              payload=None,
              gt_collector_timestamp=None,
              lt_collector_timestamp=None):
        """Yields a lists of events that match filters.

        :rtype: list of vitrage.storage.sqlalchemy.models.Event
        """
        raise NotImplementedError('query events is not implemented')

    def delete(self,
               event_id=None,
               collector_timestamp=None,
               gt_collector_timestamp=None,
               lt_collector_timestamp=None):
        """Delete all events that match the filters."""
        raise NotImplementedError('delete events is not implemented')


@six.add_metaclass(abc.ABCMeta)
class GraphSnapshotsConnection(object):
    def create(self, graph_snapshot):
        """Create a new graph snapshot.

        :type graph_snapshot: vitrage.storage.sqlalchemy.models.GraphSnapshot
        """
        raise NotImplementedError('create graph snapshot not implemented')

    def update(self, graph_snapshot):
        """Update a graph snapshot.

        :type graph_snapshot: vitrage.storage.sqlalchemy.models.GraphSnapshot
        """
        raise NotImplementedError('update graph snapshot not implemented')

    def query(self, timestamp=None):
        """Yields latest graph snapshot taken until timestamp.

        :rtype: vitrage.storage.sqlalchemy.models.GraphSnapshot
        """
        raise NotImplementedError('query graph snapshot not implemented')

    def delete(self, timestamp=None):
        """Delete all graph snapshots taken until timestamp."""
        raise NotImplementedError('delete graph snapshots not implemented')
