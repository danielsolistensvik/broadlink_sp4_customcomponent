"""
The "hello world" custom component.
This component implements the bare minimum that a component should implement.
Configuration:
To use the hello_word component you will need to add the following to your
configuration.yaml file.
hello_world:
"""

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "sp4"
"""
def setup(hass, config):
    # States are in the format DOMAIN.OBJECT_ID.
    # Return boolean to indicate that initialization was successfully.
    return True#"""