#include "lists.h"
/**
 * check_cycle - checks and looks for a cycle in a linked list
 * 
 * @list: the first element in  the linked list
 * Return - either 1 or 0 based on the condition met.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *check = temp;

	if (list->next == NULL)
	{
		return (0);
	}
	if (list == NULL)
	{
		return (0);
	}

	while (temp && temp->next)
	{
		temp = temp->next->next;
		check = check->next;
		if (check == temp)
		{
			return (1);
		}
	}
	return (0);
}
