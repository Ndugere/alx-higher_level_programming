#include <Python.h>

void print_python_list(PyObject *py_list);
void print_python_bytes(PyObject *py_bytes);

/**
 * print_python_list - Prints basic info about Python lists.
 * @py_list: A PyObject list object.
 */
void print_python_list(PyObject *py_list)
{
	int size, alloc, index;
	const char *type;
	PyListObject *list = (PyListObject *)py_list;
	PyVarObject *var = (PyVarObject *)py_list;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @py_bytes: A PyObject byte object.
 */
void print_python_bytes(PyObject *py_bytes)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)py_bytes;

	printf("[.] bytes object info\n");
	if (strcmp(py_bytes->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)py_bytes)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)py_bytes)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)py_bytes)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
