#include "lists.h"
/**
 * length - gets length of linked list.
 * @head: head of linked list
 * Return: the length of the list.
 */
int length(listint_t *head)
{
	int i;

	i = 0;
	while (head)
	{
		head = head->next;
		++i;
	}
	return (i);
}
/**
 * is_palindrome - checks if linked list is palidrome.
 * @head: pointer to head of linked list
 * Return: 1 if it is palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *prior, *next;
	int i, len, half;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	next = (*head)->next;
	prior = NULL;
	len = length(*head);
	half = len / 2;
	i = 0;
	for (i = 0; i < half - 1; ++i)
	{
		current->next = prior;
		prior = current;
		current = next;
		next = next->next;
	}
	current->next = prior;
	if (len % 2)
		next = next->next;
	for (i = 0; i < half - 1; ++i)
	{
		if (current->n != next->n)
			return (0);
		current = current->next;
		next = next->next;
	}

	return (1);
}
