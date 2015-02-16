def solution(filename, path='woodward_colella_blast'):
    """
    This function reads the solution stored in an 
    ascii file written by pyclaw.
    """
    import sys
    
    # Concatenate path and file name
    pathfilename = path + "/" + filename

    try:
        f = open(pathfilename,"r")
    except IOError as e:
        print("({})".format(e))
        sys.exit()

    # Read file header
    # The information contained in the first two lines are not used.
    unused = f.readline()  # grid_number
    unused = f.readline()  # AMR_level

    # Read mx, my, xlow, ylow, dx and dy
    line = f.readline()
    sline = line.split()
    mx = int(sline[0])

    line = f.readline()
    sline = line.split()
    xlower = float(sline[0])

    line = f.readline()
    sline = line.split()
    dx = float(sline[0])

    # Grid:
    xupper = xlower + mx * dx
    xc = np.linspace(xlower+dx/2.,xupper-dx/2.,mx)  
    
    # Read solution
    # Define arrays of conserved variables
    q = np.zeros((mx,3))

    line = f.readline()
    for j in range(mx):
        line = f.readline()
        q[j,:] = np.array(map(float, line.split()))
    
    return q, xc

def time(filename, path='woodward_colella_blast'):
    """
    This function reads the time stored in an 
    ascii file written by pyclaw.
    """
    from clawpack import pyclaw
    import sys
    
    # Concatenate path and file name
    pathfilename = path + "/" + filename

    try:
        f = open(pathfilename,"r")
    except IOError as e:
        print("({})".format(e))
        sys.exit()

    # Read time
    line = f.readline()
    sline = line.split()
    t = float(sline[0])

    return t
