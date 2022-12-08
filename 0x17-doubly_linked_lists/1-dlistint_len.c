#include "lists.h"

/**
  *dlistint_len - get num of elements in a dynamically
  *linked list
  *
  *@h: first element of the linked list
  *Return: num of elements
  */
size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	while(h != NULL)
	{
		i++;
		h = h -> next;
	}
	return (i);
}
