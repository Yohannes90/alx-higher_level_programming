#include lists.h

/**
 * check_cycle - checks if there is some node in the list that can be reached
 * again by continuously following the next pointer
 * @list: pointer to the begining of the singly linked list to be checked
 *
 * Return: 1 if there is cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	current = list;
	check = current->next;
	while (current != NULL && check->next != NULL && check->next->next != NULL)
	{
		if (current == check)
		{
			return (1);
		}
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
