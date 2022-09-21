#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *high, *low, *new;
    low = (*head);
    new = malloc(sizeof(listint_t));
    if (!new)
    {
        return NULL;
    }
    new->n = number;
    if (!(*head))
    {
        return NULL;
    }
    while (high && low && high->next)
    {
        low = low->next;
        high = low->next;
        if (low->n < number && high->n > number)
        {
            low->next = new;
            new->next = high;
            return (new);
        }
    }

    return (NULL);
}