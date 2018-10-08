class  Todo(object):
	"""docstring for  Todo"""
	def __init__(self, created_at, name):
		super( Todo, self).__init__()
		self.created_at = created_at
		self.name = name
	def add_task(self):
		pass
	def show_task(self):
		pass
	def delete_task(self):
		pass

class HomeTodo(Todo):
	"""docstring for ClassName"""
	def __init__(self, category):
		super(HomeTodo, self).__init__()
		self.category = category
	def show_single_task(task_id):
		pass
		
		