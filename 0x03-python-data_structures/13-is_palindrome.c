#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the first node of a linked list
 * Return: 0 if it is not a palinfrome and 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *new;
	int i, count = 0;

	temp = new = (*head);
	if ((*head) == NULL || (*head)->next == NULL)
	{
		return  (1);
	}
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	int array[count];

	for (i = 0; i < count; i++)
	{
		array[i] = new->n;
		new = new->next;
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
