from django.shortcuts import render
from django.http import JsonResponse
from .algorithms import BinaryTree

tree = BinaryTree()  # Single instance of the tree

class TreeNode:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right

    def to_dict(self):
        """Convert the tree node to a dictionary for JSON response."""
        return {
            "id": self.id,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }


def build_tree_structure(nodes):
    """Builds a binary tree from a list of nodes."""
    if not nodes:
        raise ValueError("No nodes provided.")

    # Create a dictionary to hold references to the nodes
    node_map = {node["id"]: TreeNode(node["id"]) for node in nodes}

    # Link the nodes
    root = None
    for node in nodes:
        current = node_map[node["id"]]
        if node.get("left") is not None:
            current.left = node_map.get(node["left"])
        if node.get("right") is not None:
            current.right = node_map.get(node["right"])

        # Assume the first node is the root (or implement your own root-detection logic)
        if root is None:
            root = current

    return root.to_dict()

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def build_tree(request):
    if request.method == "POST":
        try:
            # Parse the request body
            data = json.loads(request.body)
            nodes = data.get("nodes")

            if not nodes:
                return JsonResponse({"error": "No nodes provided."}, status=400)

            # Build the tree using the implemented function
            tree = build_tree_structure(nodes)

            # Return the tree as a JSON response
            return JsonResponse({"tree": tree}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        # For GET requests, return an informational message
        return JsonResponse({"message": "This endpoint accepts POST requests to build a tree."})

def get_tree(request):
    """
    Fetch the complete tree structure for visualization.
    """
    tree_structure = tree.traverse_tree(tree.root)
    return JsonResponse(tree_structure, safe=False)

def traverse_tree(request):
    """
    Perform a tree traversal operation and return the result.
    """
    order = request.GET.get("order", "inorder")
    if order == "inorder":
        result = tree.inorder(tree.root)
    else:
        result = []
    return JsonResponse({"order": result})
