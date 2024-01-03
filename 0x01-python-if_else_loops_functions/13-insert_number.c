#include "lists.h"
/**
  *insert_node - insert new node in sorted singly linked list
  *
  *@head: pointer to list
  *@number: number to be inserted in list
  *Return: new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = (listint_t *)malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		listint_t *temp = *head;

		while (temp->next != NULL && temp->next->n < number)
		{
			temp = temp->next;
		}
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
