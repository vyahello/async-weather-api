import pytest
from _pytest.mark import MarkDecorator

unit: MarkDecorator = pytest.mark.unit
smoke: MarkDecorator = pytest.mark.smoke
async_: MarkDecorator = pytest.mark.asyncio
parametrize: MarkDecorator = pytest.mark.parametrize
