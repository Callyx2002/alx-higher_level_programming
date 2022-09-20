#include "lists.h"
/**
 * check_cycle - checks and looks for a cycle in a linked list
 * 
 * @list: the first element in  the linked list
 * Return - either 1 or 0 based on the condition met.
 */
int check_cycle(listint_t *list)
{
	listint_t *check, *temp;
	check = list;
	
	if (!list)
	{
		return (0);
	}
	temp = list->next;
	while (temp && temp->next)
	{
		if (check == temp)
		{
			return (1);
		}
		temp = temp->next->next;
		check = check->next;
	}
	return (0);
}
