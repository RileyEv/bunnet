from abc import abstractmethod
from typing import Any, Dict, Mapping, Optional, Union

from pymongo.client_session import ClientSession

from bunnet.odm.bulk import BulkWriter
from bunnet.odm.fields import ExpressionField
from bunnet.odm.operators.update.general import (
    CurrentDate,
    Inc,
    Set,
)


class UpdateMethods:
    """
    Update methods
    """

    @abstractmethod
    def update(
        self,
        *args: Mapping[str, Any],
        session: Optional[ClientSession] = None,
        bulk_writer: Optional[BulkWriter] = None,
        **kwargs,
    ):
        return self

    def set(
        self,
        expression: Dict[Union[ExpressionField, str], Any],
        session: Optional[ClientSession] = None,
        bulk_writer: Optional[BulkWriter] = None,
        **kwargs,
    ):
        """
        Set values

        Example:

        ```python

        class Sample(Document):
            one: int

        Document.find(Sample.one == 1).set({Sample.one: 100})

        ```

        Uses [Set operator](https://roman-right.github.io/bunnet/api/operators/update/#set)

        :param expression: Dict[Union[ExpressionField, str], Any] - keys and
        values to set
        :param session: Optional[ClientSession] - pymongo session
        :param bulk_writer: Optional[BulkWriter] - bulk writer
        :return: self
        """
        return self.update(
            Set(expression), session=session, bulk_writer=bulk_writer, **kwargs
        )

    def current_date(
        self,
        expression: Dict[Union[ExpressionField, str], Any],
        session: Optional[ClientSession] = None,
        bulk_writer: Optional[BulkWriter] = None,
        **kwargs,
    ):
        """
        Set current date

        Uses [CurrentDate operator](https://roman-right.github.io/bunnet/api/operators/update/#currentdate)

        :param expression: Dict[Union[ExpressionField, str], Any]
        :param session: Optional[ClientSession] - pymongo session
        :param bulk_writer: Optional[BulkWriter] - bulk writer
        :return: self
        """
        return self.update(
            CurrentDate(expression),
            session=session,
            bulk_writer=bulk_writer,
            **kwargs,
        )

    def inc(
        self,
        expression: Dict[Union[ExpressionField, str], Any],
        session: Optional[ClientSession] = None,
        bulk_writer: Optional[BulkWriter] = None,
        **kwargs,
    ):
        """
        Increment

        Example:

        ```python

        class Sample(Document):
            one: int

        Document.find(Sample.one == 1).inc({Sample.one: 100})

        ```

        Uses [Inc operator](https://roman-right.github.io/bunnet/api/operators/update/#inc)

        :param expression: Dict[Union[ExpressionField, str], Any]
        :param session: Optional[ClientSession] - pymongo session
        :param bulk_writer: Optional[BulkWriter] - bulk writer
        :return: self
        """
        return self.update(
            Inc(expression), session=session, bulk_writer=bulk_writer, **kwargs
        )
