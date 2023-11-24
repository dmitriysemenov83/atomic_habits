from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        related_habit = data.get('related_habit')
        reward = data.get('reward')
        is_pleasant = data.get('is_pleasant')

        if is_pleasant and (related_habit or reward):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки.")

        if related_habit and reward:
            raise serializers.ValidationError(
                "Нельзя одновременно выбирать связанную привычку и указывать вознаграждение.")

        time_to_complete = data.get('time_to_complete')

        if time_to_complete > 120:
            raise serializers.ValidationError("Время выполнения не должно превышать 120 секунд.")

        related_habit = data.get('related_habit')

        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки.")

        period = data.get('period')

        if period > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')

        return data
