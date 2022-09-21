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
    high =  (*head)->next;
    if ((*head)->next == NULL)
    {
        if ((*head)->n > number)
        {
            (*head)->next = new;
            new->next = NULL;
        }
        else
        {
            new = (low);
            new->next = (*head);
            (*head)->next = NULL;
        }
    }
    while (low && high)
    {
        high = high->next;
        low = low->next;
        if (number > low->n && number < high->n)
        {
            low->next = new;
            new->next = high;
            return (new);
        }
        
    }

    return (NULL);
}