class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self._find_by_id(self.root, id)


  def _find_by_id(self, node, id):
      if node.get('id') == id:
          return node
      
      if 'children' in node and node['children']:
          for child in node['children']:
              result = self._find_by_id(child, id)
              if result:
                  return result
      
      return None