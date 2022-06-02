from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    measure = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'

    def str(self):
        return f'{self.name}, {self.measure}'


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Тег',
        null=False,
        unique=True
        )
    slug = models.SlugField(verbose_name='Ссылка', unique=True)
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет',
        unique=True
        )

    class Meta:
        verbose_name = 'Хэштэг'

    def str(self):
        return f'{self.name}'


class Recipes(models.Model):
    text = models.TextField(verbose_name='Текст')
    name = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    cooking_time = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1, 'Значение не может быть меньше 1')],
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Хештеги',
        related_name='recipes',
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='project/',
        blank=True
    )
    ingredients = models.ManyToManyField(
        Ingredients,
        verbose_name='Ингредиенты',
        through='IngredientAmount',
        related_name='recipes',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        related_name='ingredients_in_recipe',
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='ingredients_of_recipe',
        verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество ингредиентов'
    )

    class Meta:
        verbose_name = 'Количество'

    def str(self):
        return f'{self.amount} {self.ingredient} in {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shoppingcart'
        )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='purchases_of_shoppingcart'
        )

    class Meta:
        verbose_name = 'Список покупок'

    def str(self):
        return f'Shopping Cart of {self.user}:{self.recipe}'


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourites_of_user'
        )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='purchases_of_favourites'
        )

    class Meta:
        verbose_name = 'Избранное'

    def str(self):
        return f'Favourite of {self.user}:{self.recipe.name}'
