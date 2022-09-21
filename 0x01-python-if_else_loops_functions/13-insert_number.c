#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *high, *low, *new;
    high = low = (*head);
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

    if ((*head)->n < number)
    {
        low = new;
        new->next = (*head);
        return (new);
    }
    while (high && low)
    {
        
    
        low = low->next;
        high = low->next;
    }

    return (NULL);
}