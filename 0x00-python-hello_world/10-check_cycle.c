#include "lists.h"
/**
  *check_cycle - check if a linked list has a
  *cycle
  *
  *@list: pointer to a linked list
  *Return: 1 if true and 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *second = list;

	/*iterate throught the linked list using pinter t list*/
	while (second != NULL && second->next != NULL)
	{
		/* move first pointer one step */
		temp = temp->next;
		/* move second pointer two steps */
		second = second->next->next;
		/* Check if the pointers meet (cycle detected) */
		if (temp == second)
			return (1); /*cycle detected*/
	}
	/* no cycle foind */
	return (0);
}
