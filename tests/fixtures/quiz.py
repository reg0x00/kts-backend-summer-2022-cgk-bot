import datetime

import pytest

from app.bot.models import TgUsersModel, SessionModel, TgUserChatModel, SessionCurrentQuestionModel
from app.bot.models_dc import User, BotSession, SessionQuestion
from app.quiz.models import (
    Answer,
    AnswerModel,
    Question,
    QuestionModel,
)


@pytest.fixture
def answers(store) -> list[Answer]:
    return [
        Answer(title="1"),
        Answer(title="2"),
        Answer(title="3"),
        Answer(title="4"),
    ]


@pytest.fixture
async def question_1(db_session) -> Question:
    title = "Which battle ended the French’s attempts to dominate Europe?"
    async with db_session.begin() as session:
        question = QuestionModel(
            title=title,
            answers=[
                AnswerModel(
                    title="The Battle of Waterloo",
                ),
            ],
        )

        session.add(question)

    return Question(
        id=question.id,
        title=title,
        answers=[
            Answer(
                title=a.title,
            )
            for a in question.answers
        ],
    )


@pytest.fixture
async def question_2(db_session) -> Question:
    title = "Storming the beaches of Normandy is more commonly known as?"
    async with db_session.begin() as session:
        question = QuestionModel(
            title=title,
            answers=[
                AnswerModel(
                    title="D-Day",
                ),
            ],
        )

        session.add(question)

    return Question(
        id=question.id,
        title=question.title,
        answers=[
            Answer(
                title=a.title,
            )
            for a in question.answers
        ],
    )


@pytest.fixture
async def question_3(db_session) -> Question:
    title = "How long did the “100 year War” last?"
    async with db_session.begin() as session:
        question = QuestionModel(
            title=title,
            answers=[
                AnswerModel(
                    title="116 years",
                ),
            ],
        )

        session.add(question)

    return Question(
        id=question.id,
        title=question.title,
        answers=[
            Answer(
                title=a.title,
            )
            for a in question.answers
        ],
    )


@pytest.fixture
async def session_1(db_session) -> BotSession:
    async with db_session.begin() as session:
        user_chat = SessionModel(
            chat_id=120
        )
        session.add(user_chat)

    return BotSession(
        chat_id=user_chat.chat_id
    )


@pytest.fixture
async def active_session_1(session_1: BotSession, db_session, user_chat_1: User, question_1: Question) -> BotSession:
    async with db_session.begin() as session:
        sess = SessionCurrentQuestionModel(
            session_id=session_1.chat_id,
            question_id=question_1.id,
            started_date=int(datetime.datetime.now().timestamp()),
            lead=user_chat_1.id,
        )
        session.add(sess)

    return BotSession(
        chat_id=session_1.chat_id,
        session_question=SessionQuestion(
            question=question_1,
            started_date=sess.started_date,
            completed_questions=sess.completed_questions,
            correct_questions=sess.correct_questions,
            lead=user_chat_1
        )
    )


@pytest.fixture
async def session_2(db_session) -> BotSession:
    async with db_session.begin() as session:
        user_chat = SessionModel(
            chat_id=130
        )
        session.add(user_chat)

    return BotSession(
        chat_id=user_chat.chat_id
    )


@pytest.fixture
async def user_chat_1(db_session) -> User:
    async with db_session.begin() as session:
        user = TgUsersModel(
            id=100,
            uname="asd",
            chat=[TgUserChatModel(chat_id=120)]
        )
        session.add(user)

    return User(
        id=user.id,
        chat_id=[120],
        uname="asd"
    )


@pytest.fixture
async def user_chat_2(db_session) -> User:
    async with db_session.begin() as session:
        user = TgUsersModel(
            id=200,
            uname="asd",
            chat=[TgUserChatModel(chat_id=120)]
        )
        session.add(user)

    return User(
        id=user.id,
        chat_id=[120],
        uname="asd"
    )


@pytest.fixture
async def user_chat_3(db_session) -> User:
    async with db_session.begin() as session:
        user = TgUsersModel(
            id=300,
            uname="asd",
            chat=[TgUserChatModel(chat_id=120)]
        )
        session.add(user)

    return User(
        id=user.id,
        chat_id=[120],
        uname="asd"
    )
