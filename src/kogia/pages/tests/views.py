# Copyright 2017-2023 Pascal Pepe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Views for testing the Pages application."""

from kogia.pages.tests.models import PageTranslation
from kogia.pages.views import PageDetail, PageList


class PageMixin:
    """A mixin for views manipulating pages."""

    model = PageTranslation


class PageDetail(PageMixin, PageDetail):
    """View that displays a page."""


class PageList(PageMixin, PageList):
    """View that displays the list of pages."""
