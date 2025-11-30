from .models import Book, Review


class BookService:

    @staticmethod
    def calculate_average_rating(book_id):
        reviews = Review.objects.filter(book_id=book_id)

        if not reviews.exists():
            return None

        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / reviews.count()

        return average_rating

    @staticmethod
    def is_popular(book_id, threshold=4):
        average_rating = BookService.calculate_average_rating(book_id)

        if average_rating is None:
            return None

        return average_rating >= threshold
