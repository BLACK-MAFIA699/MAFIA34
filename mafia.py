
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import ashok12
elif bit == '32bit':
    import ashok12