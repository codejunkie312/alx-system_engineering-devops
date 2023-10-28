#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinit_while - run an infinite while loop
 * Return: Always 0
 */
int infinit_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			exit(0);
		}
		else
		{
			perror("fork");
			return (1);
		}
	}

	infinit_while();
	return (0);
}
