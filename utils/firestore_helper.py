# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Firestore Helper.
"""

import logging

from google.cloud import firestore

logging.basicConfig()
logging.root.setLevel(logging.INFO)


class FirestoreHelper:
  """Firestore helper to read and write Firestore data.
  """

  def __init__(self):
    self.db_name = "topic-mine-settings-database"
    self.collection_name = "topic-mine-settings-collection"
    self.document_id = "topic-mine-settings-document"
    self.db = firestore.Client(database=self.db_name)

  def get_settings(self):
    """Retrieve document data from Firestore or None.

    Returns:
        A dictionary containing the document data, or None if an error occured.
    """
    try:
      doc_ref = self.db.collection(self.collection_name).document(self.document_id)
      doc = doc_ref.get()

      if doc.exists:
        return doc.to_dict()
      else:
        return None
    except Exception:
      logging.exception("Unexpected error in get_settings:")
      return None

  def save_settings(self, settings):
    """Writes data to the existing Firestore settings document.

    Args:
      settings: Dictionary of data to write to the document.
    """
    try:
      doc_ref = self.db.collection(self.collection_name).document(self.document_id)
      doc_ref.set(settings)
    except Exception as e:
      logging.exception("Unexpected error in save_settings:")
      raise e
