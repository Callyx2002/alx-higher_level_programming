#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp = (*head);
	int i, count = 0;

	if (!(*head) && (*head)->next == NULL)
		return (1);
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	temp = (*head);
	int array[count];

	for (i = 0; i < count; i++)
	{
		array[i] = temp->n;
	}

	for (i = 0; i < (count / 2); i++)
	{
		if (array[i] != array[count - 1 - i])
		{
			return (0);
		}
	}
	return (1);
}
