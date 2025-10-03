from sqlalchemy.orm import Session
from app.schemas import ArticleCreate
from app.crud import create_article


def create_article_f(db: Session):
    
    article = ArticleCreate(
        title="Random article",
        content= """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sed ullam necessitatibus velit ducimus quasi laborum repellendus assumenda delectus nam facilis, laudantium voluptate quisquam, sapiente voluptatem ipsum impedit porro provident.
        """
    )
    
    return create_article(db=db, data=article)