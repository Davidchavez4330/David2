def vector_add(vector_a,vector_b):
  """Is the sum of the two vectors.
  
  This function takes in two vectors, representd as lists, then computes their sum and returns it as a list.

  Args:
    vector_a: An arbitrary vector of  arbitrary length. Represented by a list.
    vector_b: An arbitrary vector of the same length as vector_a. Repesented by a list.

  Returns:
    A list of the same length as vector_a which is the sum of the two input vectors.
  """

  result = [0]*len(vector_a)
  for element in range(len(vector_a)):
    result[element] = vector_a[element] + vector_b[element]
  return result
 
  
def complex_conjugate(scalar):
  """Compute the conjugate of a complex number.

  This function takes in a complex number as its input and replaces the real part of its output with the real part of its input and replaces the imaginary part of its output with the conjuate part of the imaginary part of its input.

  Args:
    scalar: A complex number. 
  Returns:
    scalar: The complex conjugate of our input.
  """
  result = scalar.real
  result = result - scalar.imag*1j
  return result



def scalarVecMulti(scalar,vector):
  """Computes scalar vector multiplication

  Multiplies every element a vector by a scalar and returns the result.

  Args:
    scalar: a number
    vector: A list of numbers respresting a vector.

  Returns:
    A list of numbers respresting a vector.
    """
  result =  [0]*len(vector)
  for iterator in range(len(result)):
    result[iterator] = scalar*vector[iterator]
  return result
 
def dot(vector01,vector02):
  """Computes the dot product

  Takes in two vectors and computees their dot product.

  Args:
    vector01: A list of real numbers represting a vector
    vector02: a list of real numbers of the same dimension as vector01 also respresenting a   vector.

  Returns:
    the dot product of the inputs,
    """
  result = 0 
  for iterator in range(len(vector01)):
    result = result + conjugate(vector01[iterator])*vector02[iterator])
  return result

def two_norm(vector):
  """Calculates the 2-norm of a vector.

  Sum the squares of the elements of a given vector and returns the square root of the sum.

  Args:
    vector: A list of real numbers.
  Returns:
    A  real scalar which is the 2-norm of the given vector.
  """
  result = 0 
  for element in range(len(vector)):
    result = result + (vector[element]**2)
  result = result**(1/2)
  return result

def normalize(vector):
  """Normalize a given vector.

  Checks to see if the vector is normal or the zero vector. If not the vector is divided by   its norm.

  Args:
    vector: A list of numbers respresenting a vector.
  Returns:
    A normalized vector if the input vector was not the zero vector. Prints an error otherwise.
  """

  norm = two_norm(vector)
  if (norm == 0):
    print("Invalid Input")
  elif (norm == 1):
    return vector
  else: 
    return scalarVecMulti((1/norm),vector)  


def orthognalDecomp(OrthoSet,vector):
  """Computes an orthogonal vector.

  This function computes the orthognal decomposition of vector with respect to Orthoset.

  Args:
    OrthoSet: A list of lists, where each element represents a vector and the list as a     whole is orthonormal.

    vector: A vector of compatabile dimensions to the vectors in OrthoSet.

  Returns: 
  A vector which is orthogonal to the vectors in OrthoSet.
  """

  result = vector
  for iterator in range(len(OrthoSet)):
    tempScalar = dot(OrthoSet[iterator],vector)
    tempVector = scalarVecMulti(-tempScalar,OrthoSet[iterator])
    result = vectorAdd(result,tempVector)
  return result    